---
id: UNC@20.15.2@MMLCommand@DSP TZLST
type: MMLCommand
name: DSP TZLST（显示多时区参数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TZLST
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 多时区管理
- 多时区参数
status: active
---

# DSP TZLST（显示多时区参数）

## 功能

**适用网元：SGSN**

此命令用于查询某个时区是否进入夏令时。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TZID | 时区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询时区信息的索引。<br>取值范围：1～24<br>默认值：无 |

## 操作的配置对象

- [多时区参数（TZLST）](configobject/UNC/20.15.2/TZLST.md)

## 使用实例

查询 “时区标识” 为 “1” 的时区信息：

DSP TZLST: TZID=1;

```
%%DSP TZLST: TZID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
          时区标识  =  1
              时区  =  GMT+01:00
夏令时偏移量(小时)  =  1
(结果个数 = 1)

---    END
```

查询多条时区信息：

DSP TZLST:;

```
%%DSP TZLST:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
 时区标识  时区       夏令时偏移量(小时)

 1         GMT+03:30  0                 
 2         GMT+05:45  0                 
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示多时区参数(DSP-TZLST)_26305402.md`
