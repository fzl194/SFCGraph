---
id: UNC@20.15.2@MMLCommand@LST RGINFO
type: MMLCommand
name: LST RGINFO（显示费率组信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RGINFO
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
- 流量统计
status: active
---

# LST RGINFO（显示费率组信息）

## 功能

**适用NF：NCG**

该命令用于查询NCG用户话单所属的费率组信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RGID | 费率组ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示用户话单所属的费率组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [费率组信息（RGINFO）](configobject/UNC/20.15.2/RGINFO.md)

## 使用实例

查询话单所属费率组信息：

```
LST RGINFO:;
```

```
RETCODE = 0  操作成功

结果如下:
---------
  费率组ID  =  33
费率组名称  =  RG33
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示费率组信息（LST-RGINFO）_51174324.md`
