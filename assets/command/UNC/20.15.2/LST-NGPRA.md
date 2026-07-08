---
id: UNC@20.15.2@MMLCommand@LST NGPRA
type: MMLCommand
name: LST NGPRA（查询5G PRA）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPRA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 网络开放管理
- 5G PRA管理
- 5G PRA标识管理
status: active
---

# LST NGPRA（查询5G PRA）

## 功能

**适用NF：AMF**

该命令用于查询5G PRA基本信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示PRA区域的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是8388608~16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G PRA（NGPRA）](configobject/UNC/20.15.2/NGPRA.md)

## 使用实例

- 查询系统中当前配置的5G PRA信息：
  ```
  %%LST NGPRA:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
      PRA标识  =  8388616
     区域类型  =  公网区域
     描述信息  =  for EastLake Campus
  (结果个数 = 1)

  ---    END
  ```
- 查询系统内当前配置“PRA标识”为“8388627”的5G PRA信息：
  ```
  %%LST NGPRA: PRAID=8388627;%%
  RETCODE = 0  操作成功

  结果如下
  --------
      PRA标识  =  8388627
     区域类型  =  公网区域
     描述信息  =  for Shanghai Campus
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G-PRA（LST-NGPRA）_44007016.md`
