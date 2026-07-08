---
id: UNC@20.15.2@MMLCommand@LST MECAREA
type: MMLCommand
name: LST MECAREA（查询5G MEC区域信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MECAREA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 本地特色业务区域管理
- 本地特色业务区域标识管理
status: active
---

# LST MECAREA（查询5G MEC区域信息）

## 功能

**适用NF：AMF**

该命令用于查询5G MEC区域信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域标识 | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识AMF服务的某个区域（例如：商场）。其服务范围可以通过ADD MECAREATAI或ADD MECAREAGNB进行配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无<br>配置原则：<br>当通过RMV MECAREA命令删除“AREAID”区域成员时，请执行LST MECAREATAI和LST MECAREAGNB命令，确保中“AREAID”未被索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MECAREA]] · 5G MEC区域信息（MECAREA）

## 使用实例

查询5G MEC区域信息，执行如下命令：

```
%%LST MECAREA:;%%
RETCODE = 0  操作成功

结果如下
--------
    区域标识  =  1
    服务范围  =  West Lake
    区域类型  =  公网区域
    描述信息  =  West Lake
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MECAREA.md`
