---
id: UNC@20.15.2@MMLCommand@LST PERFCHKSWITCH
type: MMLCommand
name: LST PERFCHKSWITCH（查询性能统计核查开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFCHKSWITCH
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 性能管理
- 性能统计核查
status: active
---

# LST PERFCHKSWITCH（查询性能统计核查开关）

## 功能

**适用网元：SGSN、MME**

该命令用于查询性能统计核查开关。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [性能统计核查开关（PERFCHKSWITCH）](configobject/UNC/20.15.2/PERFCHKSWITCH.md)

## 使用实例

查询核查开关：

LST PERFCHKSWITCH:;

```
%%LST PERFCHKSWITCH:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
核查开关  =  打开
核查周期  =  30          
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询性能统计核查开关(LST-PERFCHKSWITCH)_72225877.md`
