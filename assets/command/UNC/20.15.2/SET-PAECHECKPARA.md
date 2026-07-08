---
id: UNC@20.15.2@MMLCommand@SET PAECHECKPARA
type: MMLCommand
name: SET PAECHECKPARA（设置PAE寻呼反压流控检测参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PAECHECKPARA
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- PAE寻呼反压流控管理
status: active
---

# SET PAECHECKPARA（设置PAE寻呼反压流控检测参数）

## 功能

**适用NF：MME、AMF**

该命令用于设置LINK节点相关资源过载检测参数，包括link-pod内pBuf资源和PAE与虚拟交换机间消息发送队列所使用的检测周期、检测次数等信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHECKINTERVAL | 检测间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源过载状态的检测间隔，单位为s。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1~255。<br>默认值：1s<br>配置原则： 无 |
| CHECKTIMES | 检测次数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示检测结果连续超过过载阈值或低于恢复阈值的次数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围1~255。<br>默认值：5<br>配置原则： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAECHECKPARA]] · PAE寻呼反压流控检测参数（PAECHECKPARA）

## 使用实例

设置PAE寻呼反压流控的检测间隔（s）为10：

```
SET PAECHECKPARA: CHECKINTERVAL=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PAE寻呼反压流控检测参数(SET-PAECHECKPARA)_14231878.md`
