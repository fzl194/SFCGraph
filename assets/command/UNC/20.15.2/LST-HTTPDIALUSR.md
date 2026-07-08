---
id: UNC@20.15.2@MMLCommand@LST HTTPDIALUSR
type: MMLCommand
name: LST HTTPDIALUSR（查询HTTP拨测用户信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPDIALUSR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP平台管理
status: active
---

# LST HTTPDIALUSR（查询HTTP拨测用户信息）

## 功能

该命令用以查询HTTP拨测用户信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [HTTP拨测用户信息（HTTPDIALUSR）](configobject/UNC/20.15.2/HTTPDIALUSR.md)

## 使用实例

查询HTTP服务拨测用户信息，执行如下命令：

```
%%LST HTTPDIALUSR:;%%
RETCODE = 0  操作成功

结果如下
------------------------
拨测场景   用户标识类型  用户标识起始值  用户标识终止值
灰度升级   SMF-MSISDN    401152          401153
灰度升级   SMF-IMSI      46000111111110  46000111111115
灰度升级   AMF-IMSI      46000111111110  46000111111115
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP拨测用户信息（LST-HTTPDIALUSR）_96888408.md`
