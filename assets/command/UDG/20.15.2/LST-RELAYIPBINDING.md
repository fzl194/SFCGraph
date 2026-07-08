---
id: UDG@20.15.2@MMLCommand@LST RELAYIPBINDING
type: MMLCommand
name: LST RELAYIPBINDING（查询媒体中继服务IP绑定配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RELAYIPBINDING
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继服务IP绑定配置
status: active
---

# LST RELAYIPBINDING（查询媒体中继服务IP绑定配置）

## 功能

**适用NF：UPF、PGW-U**

该命令用于显示媒体中继服务IP配置和媒体中继模板名称的绑定关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYTPLNAME | 媒体中继模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示媒体中继模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYTEMPLATE命令配置生成。<br>- 配置时需要确保RELAYTPLNAME已经配置（ADD RELAYTEMPLATE）。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYIPBINDING]] · 媒体中继服务IP绑定配置（RELAYIPBINDING）

## 使用实例

查询一组媒体中继服务IP绑定配置：

```
LST RELAYIPBINDING: RELAYTPLNAME="test";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
  媒体中继模板名称  =  test
媒体中继IP地址名称  =  testip
       配置域名称  =  NULL

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RELAYIPBINDING.md`
