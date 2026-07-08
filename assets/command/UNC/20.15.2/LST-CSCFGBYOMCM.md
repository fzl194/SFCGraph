---
id: UNC@20.15.2@MMLCommand@LST CSCFGBYOMCM
type: MMLCommand
name: LST CSCFGBYOMCM（查询业务读取OM缓存数据的配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CSCFGBYOMCM
command_category: 查询类
applicable_nf:
- PGW-C
- AMF
- SMF
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# LST CSCFGBYOMCM（查询业务读取OM缓存数据的配置）

## 功能

**适用NF：PGW-C、AMF、SMF、GGSN、SGW-C**

该命令用于查询哪些配置是通过OM缓存被业务使用的。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMLNAME | 配置命令名称 | 可选必选说明：可选参数<br>参数含义：该参数表示配置命令的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。不能为非法字符，只允许输入字母和数字，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数表示配置命令的名称，比如PLMNNS，不要输入ADD/RMV/MOD/LST等操作字符，优先LST命令名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CSCFGBYOMCM]] · 业务读取OM缓存数据的配置（CSCFGBYOMCM）

## 使用实例

查询业务进程使用的PLMNNS配置是否被指定从OM缓存读取：

```
%%LST CSCFGBYOMCM: MMLNAME="PLMNNS";%%
RETCODE = 0  操作成功

结果如下
--------
    配置命令名称  =  PLMNNS
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CSCFGBYOMCM.md`
