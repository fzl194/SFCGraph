---
id: UNC@20.15.2@MMLCommand@LST GAISOLATION
type: MMLCommand
name: LST GAISOLATION（查询Ga业务隔离配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GAISOLATION
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
- 业务隔离
status: active
---

# LST GAISOLATION（查询Ga业务隔离配置）

## 功能

**适用NF：NCG**

该命令用于查询NCG 上AP的Ga隔离配置情况。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GAISOLATIONID | Ga隔离标识 | 可选必选说明：可选参数<br>参数含义：话单存储对象标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：该参数只能由字母、数字、下划线、中划线组成。 |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| MNAME | 模块名称 | 可选必选说明：可选参数<br>参数含义：用于标识一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：<br>- 该值需要执行<br>[**LST MODULE**](../业务模块/查询业务模块（LST MODULE）_51174292.md)<br>命令，查询出存在的MNAME进行填写。<br>- 不能输入的特殊字符请参考“<br>[**特殊字符表**](../话单备份/增加话单备份（ADD CDRBACKUP）_51174244.md#ZH-CN_CONCEPT_0251174244__table_0365FEF0)<br>”。 |

## 操作的配置对象

- [Ga业务隔离配置（GAISOLATION）](configobject/UNC/20.15.2/GAISOLATION.md)

## 使用实例

查询当前已添加隔离的业务模块，示例如下：

```
LST GAISOLATION:;
```

```
RETCODE = 0  操作成功  
结果如下: 
--------- 
GA隔离标识  =  iso1     
    RU的ID  =  0   
  模块名称  =  NULL 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Ga业务隔离配置（LST-GAISOLATION）_99762889.md`
