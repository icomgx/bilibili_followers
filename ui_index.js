const { app, dialog, BrowserWindow, Menu } = require('electron')
const jsexecpy = require('jsexecpy')
const http = require('http')

jsexecpy.runpath('app.py', function ({ data, pythonpath }) { })

function msgbox(title, msg) {
  dialog.showMessageBox({
    title: title, type: 'info', message: msg
  })
}
function createWindow() {
  // msgbox('信息：', '请稍等，后台服务启动需要一定时间，5秒左右！\n另外，本程序后台原理较复杂，会启动一个Chrome浏览器窗口在后台，请手动最小化，请勿关闭！！')
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
  win.webContents.openDevTools()
  // 加载页面
  win.loadFile('pages/index.html')
}

app.whenReady().then(createWindow)
