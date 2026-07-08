---
id: UNC@20.15.2@MMLCommand@LST DOMAINSEPARATOR
type: MMLCommand
name: LST DOMAINSEPARATOR（查询域名前后缀分隔符）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DOMAINSEPARATOR
command_category: 查询类
applicable_nf:
- SMF
- GGSN
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 域名分隔符
status: active
---

# LST DOMAINSEPARATOR（查询域名前后缀分隔符）

## 功能

**适用NF：SMF、GGSN、PGW-C**

该命令用于查看已设置的前缀分割符和后缀分割符。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [域名前后缀分隔符（DOMAINSEPARATOR）](configobject/UNC/20.15.2/DOMAINSEPARATOR.md)

## 使用实例

查询已设置的前缀分隔符和后缀分隔符的配置信息：

```
%%LST DOMAINSEPARATOR:;%%
RETCODE = 0  操作成功

结果如下
--------
    前缀域名分隔符  =  @%
    后缀域名分隔符  =  #/
前缀域名分隔符开关  =  使能
后缀域名分隔符开关  =  使能

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询域名前后缀分隔符（LST-DOMAINSEPARATOR）_09654359.md`
