---
id: UNC@20.15.2@MMLCommand@LST VPROBESVRIP
type: MMLCommand
name: LST VPROBESVRIP（查询vProbe报表服务器的接入点IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VPROBESVRIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- vProbe管理
- vProbe服务器IP
status: active
---

# LST VPROBESVRIP（查询vProbe报表服务器的接入点IP地址）

## 功能

该命令用于查询vProbe报表服务器的接入点IP地址。

## 注意事项

执行命令前请确认vProbe服务处于上线状态，可通过DSP FUNCTIONSETINFO命令查询确认。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPROBESVRNAME | 报表服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定vProbe报表服务器名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPROBESVRIP]] · vProbe报表服务器的接入点IP地址（VPROBESVRIP）

## 使用实例

运营商A查询vProbe配置单据上报的报表服务器配置的接入点IP信息：

```
%%LST VPROBESVRIP:;%%
RETCODE = 0  操作成功

结果如下
--------
    报表服务器名称  =  VPROBESVR1
        接入点名称  =  ACCESS1
            IP类型  =  IPv4
报表服务器IPv4地址  =  10.180.211.253
报表服务器IPv6地址  =  ::
  报表服务器端口号  =  10500
          协议类型  =  TCP
  报表服务器用户名  =  NULL
    报表服务器密码  =  *****
报表服务器认证方式  =  NULL
报表服务器上传路径  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VPROBESVRIP.md`
