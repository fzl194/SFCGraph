---
id: UNC@20.15.2@MMLCommand@LST LCMLOG
type: MMLCommand
name: LST LCMLOG（查询网元生命周期管理日志）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LCMLOG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 版本信息
status: active
---

# LST LCMLOG（查询网元生命周期管理日志）

## 功能

本命令用于查询指定网元版本变更信息。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要按照哪个网元ID来查询。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：可以使用<br>[**LST ME**](查询网元配置信息（LST ME）_47084797.md)<br>命令查询获得。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LCMLOG]] · 网元生命周期管理日志（LCMLOG）

## 使用实例

查询网元生命周期管理日志：

```
%%LST LCMLOG: MEID=29;%% 
RETCODE = 0  操作成功

网元生命周期管理日志 
-------------------- 
网元名称  网元ID  网元类型  操作类型  操作时间             源版本号  目标版本号

test      29      TEST      安装网元  2020-08-28 22:17:45  21.1.0    null         
test      29      TEST      版本升级  2020-08-28 22:35:53  21.1.0    21.2.0       
test      29      TEST      版本回退  2020-08-28 22:36:01  21.2.0    21.1.0       
test      29      TEST      安装补丁  2020-08-28 22:36:13  21.1.0    21.1.0.1     
test      29      TEST      回退补丁  2020-08-28 22:36:20  21.1.0.1  21.1.0       
(结果个数 = 5) 

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LCMLOG.md`
