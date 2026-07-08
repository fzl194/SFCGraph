---
id: UNC@20.15.2@MMLCommand@DSP CDW
type: MMLCommand
name: DSP CDW（显示话单处理速度）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CDW
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 维护管理
status: active
---

# DSP CDW（显示话单处理速度）

## 功能

**适用NF：NCG**

该命令用于显示话单处理速度。该命令执行后，返回1分钟周期内话单处理的平均速率。

在系统新安装、健康检查或者故障处理时，可以使用该命令进行检查。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- “接入网元分组标识”可以通过[**LST CDRPROC**](../../业务配置管理/话单处理/查询话单处理（LST CDRPROC）_51174275.md)命令查询获取。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：用于表示一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- “模块名”可以通过[**LST MODULE**](../../业务配置管理/业务模块/查询业务模块（LST MODULE）_51174292.md)命令查询获取。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](../../业务配置管理/话单存储/增加话单存储（ADD CDRSTOR）_51174277.md#ZH-CN_CONCEPT_0251174277__table_0365FEF0)”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDW]] · 话单处理速度（CDW）

## 使用实例

显示所有模块的话单处理速度：

```
DSP CDW:;
```

```
 
RETCODE = 0  操作成功

结果如下:
---------
接入网元分组标识  =  PS_GROUP_1 
          模块名  =  AP66_1     
    话单处理速度  =  802        
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示话单处理速度（DSP-CDW）_51174312.md`
