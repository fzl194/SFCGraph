---
id: UDG@20.15.2@MMLCommand@LST PPPCFG
type: MMLCommand
name: LST PPPCFG（查询PPP配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PPPCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- PPP配置
status: active
---

# LST PPPCFG（查询PPP配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查看系统进行PPP协商时所使用的参数，包括系统侧与用户鉴权时使用的主机名、系统的最大接收单元、PPP协商请求的超时时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PPPCFG]] · PPP配置（PPPCFG）

## 使用实例

运营商如果需要查看当前配置的系统与PPP协商时使用的参数：

```
LST PPPCFG:;
```

```

RETCODE = 0  操作成功。

PPP配置信息:
------------
  本端主机名称  =  华为 
  最大接收单元  =  1500
超时时间（秒）  =  3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PPPCFG.md`
