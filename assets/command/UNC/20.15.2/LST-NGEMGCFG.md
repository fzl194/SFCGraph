---
id: UNC@20.15.2@MMLCommand@LST NGEMGCFG
type: MMLCommand
name: LST NGEMGCFG（查询运营商紧急呼叫功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGEMGCFG
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- 紧急呼叫业务管理
- 紧急呼叫配置
status: active
---

# LST NGEMGCFG（查询运营商紧急呼叫功能配置）

## 功能

**适用NF：AMF**

该命令用于查询指定的MNO或MVNO对应的紧急呼叫配置数据。

## 注意事项

当不输入查询条件时，显示所有记录信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGEMGCFG]] · 运营商紧急呼叫功能配置（NGEMGCFG）

## 使用实例

- 不输入查询条件，查询表中全部紧急呼叫配置的数据，执行如下命令：
  ```
  %%LST NGEMGCFG:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        运营商标识  =  0
  紧急会话创建模式  =  仅限合法用户
      数据网络名称  =  HUAWEI.COM
      切片业务类型  =  0
      切片细分标识  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询“运营商标识”为“0”的紧急呼叫配置数据，执行如下命令：
  ```
  %%LST NGEMGCFG: NOID=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        运营商标识  =  0
  紧急会话创建模式  =  仅限合法用户
      数据网络名称  =  HUAWEI.COM
      切片业务类型  =  0
      切片细分标识  =  FFFFFF
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询运营商紧急呼叫功能配置（LST-NGEMGCFG）_09652706.md`
