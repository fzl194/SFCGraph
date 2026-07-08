---
id: UNC@20.15.2@MMLCommand@LST EPLMNAREAMEM
type: MMLCommand
name: LST EPLMNAREAMEM（查询跟踪区域组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPLMNAREAMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 接入管理
- 等价PLMN区域管理
status: active
---

# LST EPLMNAREAMEM（查询跟踪区域组成员）

## 功能

**适用NF：AMF**

该命令用于查询等价PLMN的跟踪区域组成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TACGRPID | 跟踪区域组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识使用相同等价PLMN策略的跟踪区域范围。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPLMNAREAMEM]] · 跟踪区域组成员（EPLMNAREAMEM）

## 使用实例

- 查询跟踪区域组标识为20的跟踪区域组成员信息，执行如下命令：
  ```
  %%LST EPLMNAREAMEM: TACGRPID=20;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    跟踪区域组标识  =  20
  跟踪区域码起始值  =  120101
  跟踪区域码结束值  =  120102
          描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的所有区域的信息，执行如下命令：
  ```
  %%LST EPLMNAREAMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    跟踪区域组标识  =  20
  跟踪区域码起始值  =  120101
  跟踪区域码结束值  =  120102
          描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询跟踪区域组成员（LST-EPLMNAREAMEM）_78418138.md`
