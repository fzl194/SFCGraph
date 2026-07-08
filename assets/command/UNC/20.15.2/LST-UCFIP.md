---
id: UNC@20.15.2@MMLCommand@LST UCFIP
type: MMLCommand
name: LST UCFIP（查询UCF报表本地IP资源池）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UCFIP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF本地IP
status: active
---

# LST UCFIP（查询UCF报表本地IP资源池）

## 功能

该命令用于查询UCF的本地报表IP地址池。

## 注意事项

执行命令前请确认UCF服务处于上线状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UCFIP]] · UCF报表本地IP资源池（UCFIP）

## 使用实例

运营商A查询UCF配置单据上报的本地IP资源池配置信息：

```
%%LST UCFIP:;%%
RETCODE = 0  操作成功

结果如下
--------
    索引号  =  1
  协议类型  =  SFTP
    IP类型  =  IPv4
  IPv4地址  =  10.181.23.253
  IPv6地址  =  ::
起始端口号  =  2000
结束端口号  =  2001
   VPN名称  =  _public_
      描述  =  NULL

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UCFIP.md`
