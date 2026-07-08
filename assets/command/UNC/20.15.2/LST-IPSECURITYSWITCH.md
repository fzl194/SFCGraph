---
id: UNC@20.15.2@MMLCommand@LST IPSECURITYSWITCH
type: MMLCommand
name: LST IPSECURITYSWITCH（查询IP选项安全开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPSECURITYSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 安全配置
- IP安全开关
status: active
---

# LST IPSECURITYSWITCH（查询IP选项安全开关）

## 功能

该命令用于查询CSLB中IP选项安全开关配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；

## 参数

无

## 操作的配置对象

- [IP选项安全开关（IPSECURITYSWITCH）](configobject/UNC/20.15.2/IPSECURITYSWITCH.md)

## 使用实例

查询CSLB中IP选项安全开关的配置。

```
%%LST IPSECURITYSWITCH:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
      IPv4选项安全配置开关  =  IP安全开关关闭
IPv6扩展头选项安全配置开关  =  IP安全开关关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IP选项安全开关（LST-IPSECURITYSWITCH）_38232949.md`
