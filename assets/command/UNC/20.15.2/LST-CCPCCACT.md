---
id: UNC@20.15.2@MMLCommand@LST CCPCCACT
type: MMLCommand
name: LST CCPCCACT（查询融合计费Proxy基于CC处理动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CCPCCACT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 融合计费Proxy基于CC处理动作
status: active
---

# LST CCPCCACT（查询融合计费Proxy基于CC处理动作）

## 功能

**适用NF：NCG**

该命令用于查询融合计费Proxy基于CC处理动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTYPE | CC类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CC的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULT（针对未指定的CC设置处理动作）<br>- VALUE（针对CC设置处理动作）<br>默认值：无<br>配置原则：无 |
| CHGCHAR | 指定计费属性值 | 可选必选说明：该参数在"CCTYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于指定计费属性的值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~6。十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CCPCCACT]] · 融合计费Proxy基于CC处理动作（CCPCCACT）

## 使用实例

查询融合计费Proxy基于CC处理动作：

```
LST CCPCCACT:;
RETCODE = 0  操作成功

结果如下
--------
          CC类型  =  针对CC设置处理动作
  指定计费属性值  =  0x1234
指定计费属性掩码  =  0xFFFF
     是否转发OCS  =  是
Failover模板标识  =  ccpfot1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CCPCCACT.md`
