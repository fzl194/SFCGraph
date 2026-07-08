---
id: UNC@20.15.2@MMLCommand@LST CCPRGACT
type: MMLCommand
name: LST CCPRGACT（查询融合计费Proxy基于RG处理动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCPRGACT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy基于RG处理动作
status: active
---

# LST CCPRGACT（查询融合计费Proxy基于RG处理动作）

## 功能

**适用NF：NCG**

该命令用于查询融合计费Proxy基于RG处理动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RGTYPE | RG类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RG的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的费率组设置处理动作）<br>- VALUE（针对费率组设置处理动作）<br>默认值：无<br>配置原则：无 |
| RATINGGROUP | 费率组标识 | 可选必选说明：该参数在"RGTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定费率组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~9223372036854775807。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPRGACT]] · 融合计费Proxy基于RG处理动作（CCPRGACT）

## 使用实例

查询融合计费Proxy基于RG处理动作：

```
LST CCPRGACT:;
RETCODE = 0  操作成功

结果如下
--------
            RG类型  =  针对RG设置处理动作
       费率组标识  =  2000000009
   是否转发OCS  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CCPRGACT.md`
