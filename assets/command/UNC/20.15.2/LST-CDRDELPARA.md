---
id: UNC@20.15.2@MMLCommand@LST CDRDELPARA
type: MMLCommand
name: LST CDRDELPARA（查询话单删除参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRDELPARA
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
- 话单删除参数管理
status: active
---

# LST CDRDELPARA（查询话单删除参数）

## 功能

**适用NF：NCG**

该命令用于查询当前话单删除、话单备份和话单分发任务的话单删除参数信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDELOBJ | 话单删除对象 | 可选必选说明：可选参数<br>参数含义：用于修改话单删除、话单备份和话单分发三种类型任务的话单删除参数。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CDRDELTASK：话单删除。<br>- CDRBACKUP：话单备份。<br>- CDRDISTR：话单分发。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRDELPARA]] · 话单删除参数（CDRDELPARA）

## 使用实例

查询话单删除参数：

```
LST CDRDELPARA:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
话单删除对象    话单删除开始时间    话单删除时间间隔(毫秒) 

话单删除        04:00               20                     
话单备份        04:00               1000                   
话单分发        04:00               1000                   
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CDRDELPARA.md`
