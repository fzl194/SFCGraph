---
id: UNC@20.15.2@MMLCommand@DSP DBUSERINFO
type: MMLCommand
name: DSP DBUSERINFO（查询CSDB使用者信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBUSERINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 实例管理
status: active
---

# DSP DBUSERINFO（查询CSDB使用者信息）

## 功能

该命令用于查询CSDB使用者信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| LOGICGRPID | 逻辑组ID | 可选必选说明：可选参数<br>参数含义：逻辑组标识，如果不输入该参数，系统会查询CSDB的所有使用者信息。<br>数据来源：本端规划<br>取值范围：整型，0~4294967295。<br>默认值：无 |

## 操作的配置对象

- [CSDB使用者信息（DBUSERINFO）](configobject/UNC/20.15.2/DBUSERINFO.md)

## 使用实例

查询所有使用者信息：

```
%%DSP DBUSERINFO:;%%
RETCODE = 0  操作成功

操作结果如下:
-------------------------
         逻辑组ID  =  0
     业务服务类型  =  1062
       业务服务ID  =  999
 业务服务类型名称  =  NRF
         子实例ID  =  7
     容灾使用状态  =  开启容灾
         备份组ID  =  4294967295
   持久化使用状态  =  开启持久化
         部署模式  =  默认部署
(结果个数 = 1)

---    END
```

查询 “逻辑组ID” 为 “0” 的使用者信息：

```
%%DSP DBUSERINFO: LOGICGRPID=0;%%
RETCODE = 0  操作成功

操作结果如下:
-------------------------
         逻辑组ID  =  0
     业务服务类型  =  1062
       业务服务ID  =  999
 业务服务类型名称  =  NRF
         子实例ID  =  7
     容灾使用状态  =  开启容灾
         备份组ID  =  4294967295
   持久化使用状态  =  开启持久化
         部署模式  =  默认部署
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB使用者信息(DSP-DBUSERINFO)_77661137.md`
