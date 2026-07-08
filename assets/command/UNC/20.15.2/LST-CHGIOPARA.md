---
id: UNC@20.15.2@MMLCommand@LST CHGIOPARA
type: MMLCommand
name: LST CHGIOPARA（查询融合计费惯性运行参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGIOPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 惯性运行参数
status: active
---

# LST CHGIOPARA（查询融合计费惯性运行参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询融合计费惯性运行参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGIOPARA]] · 融合计费惯性运行参数（CHGIOPARA）

## 使用实例

查询融合计费惯性运行参数：

```
%%LST CHGIOPARA:;%%
RETCODE = 0  操作成功
结果如下
--------
                   N40用量上报开关  =  使能
             惯性运行FINAL上报开关  =  不使能
        惯性运行期间VT触发上报开关  =  使能
惯性运行期间CHF REAUTH触发上报开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGIOPARA.md`
