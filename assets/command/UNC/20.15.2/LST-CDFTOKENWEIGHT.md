---
id: UNC@20.15.2@MMLCommand@LST CDFTOKENWEIGHT
type: MMLCommand
name: LST CDFTOKENWEIGHT（查询cdf token权重）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDFTOKENWEIGHT
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- CDF token权重
status: active
---

# LST CDFTOKENWEIGHT（查询cdf token权重）

## 功能

**适用NF：NCG**

该命令用于查询cdf token权重。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | pod 名称 | 可选必选说明：可选参数<br>参数含义：该参数用于描述pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDFTOKENWEIGHT]] · cdf token权重（CDFTOKENWEIGHT）

## 使用实例

当查询pod名称为cgfb-pod-0上的cdf token权重：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-06-11 15:27:17+8:00
O&M    #3549
%%LST CDFTOKENWEIGHT: PODNAME="cgfb-pod-0";%%
RETCODE = 0  操作成功

结果如下
--------
 pod 名称  =  cgfb-pod-0
token权重  =  80
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询cdf-token权重（LST-CDFTOKENWEIGHT）_87520116.md`
