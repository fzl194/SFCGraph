---
id: UNC@20.15.2@MMLCommand@LST UCFSVRIP
type: MMLCommand
name: LST UCFSVRIP（查询UCF报表服务器的接入点IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UCFSVRIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF服务器IP
status: active
---

# LST UCFSVRIP（查询UCF报表服务器的接入点IP地址）

## 功能

该命令用于查询报表服务器的接入点IP地址。

## 注意事项

执行命令前请确认UCF服务处于上线状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UCFSVRNAME | UCF服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UCF服务器名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UCFSVRIP]] · UCF报表服务器的接入点IP地址（UCFSVRIP）

## 使用实例

运营商A查询UCF配置单据上报的报表服务器配置的接入点IP信息：

```
%%LST UCFSVRIP:;%%
RETCODE = 0  操作成功

结果如下
--------
    UCF服务器名称  =  UCFSVR1
       接入点名称  =  ACCESS1
           IP类型  =  IPv6
UCF服务器IPv4地址  =  0.0.0.0
UCF服务器IPv6地址  =  fc00::5
  UCF服务器端口号  =  22
         协议类型  =  SFTP
     服务器用户名  =  root
       服务器密码  =  *****
   服务器认证方式  =  无认证
   服务器上传路径  =  /paas/
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UCF报表服务器的接入点IP地址（LST-UCFSVRIP）_51253795.md`
