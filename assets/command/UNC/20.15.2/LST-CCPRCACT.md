---
id: UNC@20.15.2@MMLCommand@LST CCPRCACT
type: MMLCommand
name: LST CCPRCACT（查询融合计费Proxy结果码处理动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCPRCACT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy结果码处理动作
status: active
---

# LST CCPRCACT（查询融合计费Proxy结果码处理动作）

## 功能

**适用NF：NCG**

该命令用于查询融合计费Proxy结果码处理动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RCTYPE | RC类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RC的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的异常返回码设置处理动作）<br>- VALUE（针对指定异常返回码设置处理动作）<br>- TIMEOUT（等待响应超时）<br>- LINKFAULT（链路不可达）<br>默认值：无<br>配置原则：无 |
| CODETYPE | 指定异常返回码类型 | 可选必选说明：该参数在"RCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定异常返回码的类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~999，65535，0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPRCACT]] · 融合计费Proxy结果码处理动作（CCPRCACT）

## 使用实例

查询融合计费Proxy结果码处理动作：

```
LST CCPRCACT:;
RETCODE = 0  操作成功

结果如下
--------
            RC类型  =  针对指定的异常返回码设置处理动作
指定异常返回码类型  =  900
  Failover模板标识  =  ccpfot1
    代表对端不可用  =  FALSE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询融合计费Proxy结果码处理动作（LST-CCPRCACT）_45110918.md`
