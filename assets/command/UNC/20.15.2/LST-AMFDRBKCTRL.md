---
id: UNC@20.15.2@MMLCommand@LST AMFDRBKCTRL
type: MMLCommand
name: LST AMFDRBKCTRL（查询AMF热备容灾的控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFDRBKCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF热备容灾管理
status: active
---

# LST AMFDRBKCTRL（查询AMF热备容灾的控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF热备容灾的控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定热备容灾的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀<br>- “MSISDN_PREFIX（MSISDN前缀）”：MSISDN前缀<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定热备容灾用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"MSISDN_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定热备容灾用户的MSISDN前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFDRBKCTRL]] · AMF热备容灾控制参数（AMFDRBKCTRL）

## 使用实例

查询 所有用户的AMF热备容灾控制参数，执行如下命令：

```
%%LST AMFDRBKCTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
    用户范围  =  所有用户
    IMSI前缀  =  NULL
  MSISDN前缀  =  NULL
特征条件组合  =  不指定特征条件
数据网络名称  =  NULL
切片业务类型  =  NULL
切片细分标识  =  FFFFFF
  匹配优先级  =  255
    备份开关  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF热备容灾的控制参数（LST-AMFDRBKCTRL）_61307350.md`
