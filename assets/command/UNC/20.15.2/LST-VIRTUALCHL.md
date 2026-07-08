---
id: UNC@20.15.2@MMLCommand@LST VIRTUALCHL
type: MMLCommand
name: LST VIRTUALCHL（查询虚拟通道映射）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VIRTUALCHL
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 虚拟通道映射
status: active
---

# LST VIRTUALCHL（查询虚拟通道映射）

## 功能

**适用NF：NCG**

该命令用于查询当前系统的虚拟通道映射。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SOURCECHL | 源通道名称 | 可选必选说明：可选参数<br>参数含义：需要映射的通道名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VIRTUALCHL]] · 虚拟通道映射（VIRTUALCHL）

## 使用实例

查询当前系统的虚拟通道映射：

```
LST VIRTUALCHL:;
```

```
RETCODE = 0  操作成功  
结果如下: 
---------       
                  源通道名称  =  98/OFFLINE
            接入网元分组标识  =  PS1
                虚拟通道名称  =  90/OFFLINE 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询虚拟通道映射（LST-VIRTUALCHL）_21902793.md`
