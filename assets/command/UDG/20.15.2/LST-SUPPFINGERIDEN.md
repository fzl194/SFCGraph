---
id: UDG@20.15.2@MMLCommand@LST SUPPFINGERIDEN
type: MMLCommand
name: LST SUPPFINGERIDEN（查询SA指纹识别协议）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SUPPFINGERIDEN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- SA指纹识别
- 支持SA指纹识别的协议
status: active
---

# LST SUPPFINGERIDEN（查询SA指纹识别协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示系统支持的SA指纹识别功能的协议。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SUPPFINGERIDEN]] · SA指纹识别协议（SUPPFINGERIDEN）

## 使用实例

显示系统支持的所有SA指纹识别功能的协议：

```
LST SUPPFINGERIDEN:;
```

```

RETCODE = 0  操作成功。

支持SA指纹识别协议信息
----------------------
应用子协议名称            应用协议名称

a000dn_data               a000dn       
dolphintunnel             dolphintunnel
facebook_http_video       facebook     
facebook_messenger_im     facebook     
facebook_nonhttp_video    facebook     
facebook_others           facebook     
tor                       tor          
(结果个数 = 7)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SUPPFINGERIDEN.md`
