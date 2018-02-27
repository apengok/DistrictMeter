# -*- coding: utf-8 -*-

from django import forms
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe

#example 
class ShowHidePasswordWidget(forms.PasswordInput):
    def render(self, name, value, attrs=None):
        super().render(name, value, attrs)
        flat_attrs = flatatt(attrs)
        html = '''
            <input %(attrs)s name="password" type="password" value="%(value)s"/>
            <span id="__action__%(id)s__show_button">
            <a href="javascript:show_pwd_%(id)s()">Show</a></span>
            <span id="__action__%(id)s__hide_button" style="display:none;">
            <a href="javascript:hide_pwd_%(id)s()">Hide</a></span>
            <script type="text/javascript">
            function show_pwd_%(id)s() {
                document.getElementById("%(id)s").setAttribute('type', 'text');
                document.getElementById("__action__%(id)s__show_button")
                    .style.display="none";
                document.getElementById("__action__%(id)s__hide_button")
                    .style.display=null;
            }
            function hide_pwd_%(id)s() {
                document.getElementById("%(id)s").setAttribute('type', 'password');
                document.getElementById("__action__%(id)s__hide_button")
                    .style.display="none";
                document.getElementById("__action__%(id)s__show_button")
                    .style.display=null;
            }
            </script>
        ''' % {
            'attrs': flat_attrs,
            'id': attrs['id'],
            'value': value,
        }
        return mark_safe(html)

class CustomZoneWidget(forms.ModelChoiceField):
    def render(self,name,value,attrs=None):
        super(CustomZoneWidget,self).render(name,value,attrs)

        

        html = '''
            <div class="form-row field-zone_base">
                <div>
                    <label class="required" for="id_zone_base">Zone base:</label>
                        
                    <div class="related-widget-wrapper">
                        <select name="zone_base" required id="id_zone_base">
                              <option value="" selected>---------</option>

                              
                        </select>
                                
                            <a class="related-widget-wrapper-link change-related" id="change_id_zone_base"
                                data-href-template="/admin/dma/zonebase/__fk__/change/?_to_field=dma_id&amp;_popup=1"
                                title="Change selected zone base"><img src="/static/admin/img/icon-changelink.svg" alt="Change"/>
                            </a>
                            <a class="related-widget-wrapper-link add-related" id="add_id_zone_base"
                                href="/admin/dma/zonebase/add/?_to_field=dma_id&amp;_popup=1"
                                title="Add another zone base"><img src="/static/admin/img/icon-addlink.svg" alt="Add"/>
                            </a>
                                
                    </div>
                </div>
            </div>



        '''

        return mark_safe(html)
