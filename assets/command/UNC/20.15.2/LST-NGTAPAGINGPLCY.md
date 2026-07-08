---
id: UNC@20.15.2@MMLCommand@LST NGTAPAGINGPLCY
type: MMLCommand
name: LST NGTAPAGINGPLCY（查询5G跟踪区列表的寻呼策略配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGTAPAGINGPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG基于跟踪区列表的寻呼策略管理
status: active
---

# LST NGTAPAGINGPLCY（查询5G跟踪区列表的寻呼策略配置）

## 功能

**适用NF：AMF**

该命令用于查询基于5G跟踪区列表的寻呼策略配置数据。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | 跟踪区列表标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识一个跟踪区列表，一个跟踪区列表由一个或若干个跟踪区组成。一个跟踪区列表最多可包含16个跟踪区。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：<br>本参数配置前须先在ADD NGTALST中配置。 |

## 操作的配置对象

- [5G跟踪区列表的寻呼策略配置（NGTAPAGINGPLCY）](configobject/UNC/20.15.2/NGTAPAGINGPLCY.md)

## 使用实例

- 查询所有5G跟踪区列表的寻呼策略配置，执行如下命令：
  ```
  %%LST NGTAPAGINGPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  跟踪区列表标识  是否关闭精准寻呼  

  1               是                
  2               否                
  (结果个数 = 2)

  ---    END
  ```
- 查询“跟踪区列表标识”为“1”的5G跟踪区列表的寻呼策略配置，执行如下命令：
  ```
  %%LST NGTAPAGINGPLCY: TALISTID=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    跟踪区列表标识  =  1
  是否关闭精准寻呼  =  是
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G跟踪区列表的寻呼策略配置（LST-NGTAPAGINGPLCY）_48290736.md`
