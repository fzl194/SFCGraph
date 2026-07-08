---
id: UNC@20.15.2@MMLCommand@LST NOCENTCNCHL
type: MMLCommand
name: LST NOCENTCNCHL（查询RU通道过滤规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NOCENTCNCHL
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
- RU通道过滤规则
status: active
---

# LST NOCENTCNCHL（查询RU通道过滤规则）

## 功能

**适用NF：NCG**

该命令用于查询RU对应的通道过滤规则：

如果需要查询全部信息，请不要输入任何参数。

如果需要查询某方面的详细信息，请输入具体参数。例如，查询具体RU的过滤规则，请输入具体的RUID值。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| CHLNAME | 通道名称 | 可选必选说明：可选参数<br>参数含义：通道名称的取值为具体的通道名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无。 |

## 操作的配置对象

- [RU通道过滤规则（NOCENTCNCHL）](configobject/UNC/20.15.2/NOCENTCNCHL.md)

## 使用实例

查询RUID为64的通道过滤规则，示例如下：

```
LST NOCENTCNCHL: RUID=64;
```

```
RETCODE = 0  操作成功
结果如下:
---------
  RU的ID  =  64
通道名称  =  00/ABNORMAL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RU通道过滤规则（LST-NOCENTCNCHL）_36216641.md`
