---
id: UNC@20.15.2@MMLCommand@LST NGPRAMEM
type: MMLCommand
name: LST NGPRAMEM（查询PRA位置区成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGPRAMEM
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
- 5G PRA位置成员管理
status: active
---

# LST NGPRAMEM（查询PRA位置区成员）

## 功能

**适用NF：AMF**

该命令用于查询指定PRA或者系统中当前配置的所有PRA的位置区成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示位置区成员所归属的PRA。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是8388608~16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPRAMEM]] · PRA位置区成员（NGPRAMEM）

## 使用实例

- 查询所有的PRA区域成员，执行如下命令：
  ```
  %%LST NGPRAMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
         PRA标识  =  8388627
      位置区类型  =  5G跟踪区标识
             MCC  =  123
             MNC  =  45
  跟踪区起始编码  =  900001
  跟踪区结束编码  =  900003
  gNodeB标识长度  =  0
  gNodeB起始标识  =  0
  gNodeB结束标识  =  0
  5G小区起始标识  =  NULL
  5G小区结束标识  =  NULL
        描述信息  =  for East Lake Campus
  (结果个数 = 1)

  ---    END
  ```
- 查询标识为8388608的PRA区域成员，执行如下命令：
  ```
  %%LST NGPRAMEM: PRAID=8388608;%%
  RETCODE = 0  操作成功

  结果如下
  --------
         PRA标识  =  8388608
      位置区类型  =  5G跟踪区标识
             MCC  =  123
             MNC  =  45
  跟踪区起始编码  =  900001
  跟踪区结束编码  =  900003
  gNodeB标识长度  =  0
  gNodeB起始标识  =  0
  gNodeB结束标识  =  0
  5G小区起始标识  =  NULL
  5G小区结束标识  =  NULL
        描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGPRAMEM.md`
