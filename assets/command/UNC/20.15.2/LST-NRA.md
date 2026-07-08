---
id: UNC@20.15.2@MMLCommand@LST NRA
type: MMLCommand
name: LST NRA（查询空路由区对照表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- 空路由区信息
status: active
---

# LST NRA（查询空路由区对照表）

## 功能

**适用网元：SGSN**

查询空路由区配置表。

## 注意事项

查询的索引方式为LAI，若查询全部记录，无需输入参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LAI | LAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定空路由区所在的位置区。<br>数据来源：整网规划<br>取值范围：9～10位字符串<br>默认值：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRA]] · 空路由区对照表（NRA）

## 使用实例

查询条位置区所有的空路由区配置表记录：

**LST NRA:;**

```
%%LST NRA:;%%
RETCODE = 0  操作成功。

空路由区小区对照表
------------------
 LAI        RAC   

 100000000  0x10  
 100000001  0x10  
 100000002  0x10  
 100000003  0x10  
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRA.md`
