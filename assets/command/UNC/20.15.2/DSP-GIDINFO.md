---
id: UNC@20.15.2@MMLCommand@DSP GIDINFO
type: MMLCommand
name: DSP GIDINFO（显示POD的GID信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GIDINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- GID管理
status: active
---

# DSP GIDINFO（显示POD的GID信息）

## 功能

该命令用于查询POD的GID、TB、NPTB信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 查询场景 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询场景。<br>数据来源：本端规划<br>取值范围：<br>- “PODNAME（POD名称）”：基于POD名称查询<br>- “GID（GID）”：基于GID查询<br>- “TB（TB）”：基于TB查询<br>- “NPTB（NPTB）”：基于NPTB查询<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：该参数在"SCENE"配置为"PODNAME"时为条件必选参数。<br>参数含义：该参数用于表示POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| GID | GID | 可选必选说明：该参数在"SCENE"配置为"GID"时为条件必选参数。<br>参数含义：该参数用于表示GID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| TB | TB | 可选必选说明：该参数在"SCENE"配置为"TB"时为条件必选参数。<br>参数含义：该参数用于表示TB。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| NPTB | NPTB | 可选必选说明：该参数在"SCENE"配置为"NPTB"时为条件必选参数。<br>参数含义：该参数用于表示NPTB。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GIDINFO]] · POD的GID信息（GIDINFO）

## 使用实例

假如操作员想查询POD的GID信息，可以调用以下命令：

```
%%DSP GIDINFO: SCENE=PODNAME, PODNAME="a-pod-0";%%
RETCODE = 0  操作成功

结果如下
--------
 POD名称  =  a-pod-0
     GID  =  6000
      TB  =  2049
NPTB列表  =  1/2/3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GIDINFO.md`
