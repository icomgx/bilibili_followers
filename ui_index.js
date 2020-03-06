const { app, dialog, BrowserWindow, Menu } = require('electron')
const jsexecpy = require('jsexecpy')
const http = require('http')

jsexecpy.runpath('app.py', function({ data, pythonpath }) {})

function msgbox(title, msg) {
    dialog.showMessageBox({
        title: title,
        type: 'info',
        message: msg
    })
}

function createWindow() {
    // 创建浏览器窗口
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    })

    // 设置菜单栏
    // const template = [
    //   {
    //     label: '操作',
    //     submenu: [{
    //       label: '重新加载',
    //       accelerator: 'CmdOrCtrl+R',
    //       click: function () {
    //         win.reload()
    //       }
    //     }]
    //   }
    // ]
    // let menu = Menu.buildFromTemplate(template)
    // Menu.setApplicationMenu(menu)
    Menu.setApplicationMenu(null)
    win.webContents.openDevTools()
        // 加载页面
    win.loadFile('pages/index.html')
}

app.whenReady().then(createWindow)