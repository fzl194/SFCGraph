---
id: UNC@20.15.2@MMLCommand@LST QCIPAGINGINFO
type: MMLCommand
name: LST QCIPAGINGINFO（查询QCI寻呼策略参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QCIPAGINGINFO
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- QCI寻呼策略参数配置
status: active
---

# LST QCIPAGINGINFO（查询QCI寻呼策略参数配置）

## 功能

**适用网元：MME**

该命令用于查询QCI(QoS Class Identifier)对应的寻呼策略配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | 标准QCI值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要查询的寻呼策略对应的QCI值。<br>取值范围：1～254<br>默认值：无 |

## 操作的配置对象

- [QCI寻呼策略参数配置（QCIPAGINGINFO）](configobject/UNC/20.15.2/QCIPAGINGINFO.md)

## 使用实例

1. 不输入参数，查询所有添加的QCI寻呼策略配置信息：
  LST QCIPAGINGINFO:;
  ```
  %%LST QCIPAGINGINFO:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   标准QCI值  T3413(s)  N3413(times)  重寻呼间隔递增值(s)

   1          3         5             4                  
   2          4         4             3                  
  (结果个数 = 2)

  ---    END
  ```
2. 输入QCI参数，查询指定QCI的寻呼策略配置信息：
  LST QCIPAGINGINFO: QCI=1;
  ```
  %%LST QCIPAGINGINFO: QCI=1;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
            标准QCI值  =  1
             T3413(s)  =  3
         N3413(times)  =  5
  重寻呼间隔递增值(s)  =  4
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QCI寻呼策略参数配置(LST-QCIPAGINGINFO)_26145532.md`
