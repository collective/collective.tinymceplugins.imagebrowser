/**
 * Plone thumbnail image browsing plugin based on the ploneimage plugin 
 * (part of Products.TinyMCE 1.2.8 by Rob Gietema).
 * 
 */

(function() {
    tinymce.create('tinymce.plugins.PloneImageBrowserPlugin', {
        init : function(ed, url) {
            // Register commands
            ed.addCommand('mcePloneImage', function() {
                // Internal image object like a flash placeholder
                if (ed.dom.getAttrib(ed.selection.getNode(), 'class').indexOf('mceItem') != -1)
                    return;

                ed.windowManager.open({
                    file : url + '/ploneimage.htm',
                    width : 846 + parseInt(ed.getLang('ploneimage.delta_width', 0)),
                    height : 550 + parseInt(ed.getLang('ploneimage.delta_height', 0)),
                    inline : 1
                }, {
                    plugin_url : url
                });
            });

            // Register buttons
            ed.addButton('imagebrowser', {
                title : 'advanced.image_desc',
                cmd : 'mcePloneImage'
            });
        },

        getInfo : function() {
            return {
                longname : 'Plone thumbnail image browsing',
                author : 'Joscha Krutzki',
                authorurl : '',
                infourl : '',
                version : tinymce.majorVersion + "." + tinymce.minorVersion
            };
        }
    });

    // Register plugin
    tinymce.PluginManager.add('ploneimagebrowser', tinymce.plugins.PloneImageBrowserPlugin);
})();
