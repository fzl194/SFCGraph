---
id: UDG@20.15.2@MMLCommand@LST RELAYTLSCFG
type: MMLCommand
name: LST RELAYTLSCFG（查询媒体中继业务TLS认证配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYTLSCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继业务TLS认证配置
status: active
---

# LST RELAYTLSCFG（查询媒体中继业务TLS认证配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询Relay域名业务分别作为客户端或服务端认证属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TLSCONFIGNAME | TLS配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置该Relay业务TLS配置描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYTLSCFG]] · 媒体中继业务TLS认证配置（RELAYTLSCFG）

## 使用实例

假如需要查询媒体中继业务TLS认证配置，则命令如下：

```
LST RELAYTLSCFG:;
```

```

RETCODE = 0  操作成功
 
结果如下
------------------------
    TLS配置名称  =  douyintlscfg
 UE认证策略名称  =  ue_douyinply
CDN认证策略名称  =  NULL
     配置域名称  =  NULL
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYTLSCFG.md`
