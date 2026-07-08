---
id: UNC@20.15.2@MMLCommand@LST PLMNMATCH
type: MMLCommand
name: LST PLMNMATCH（查询MCC与MNC的归属）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLMNMATCH
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- PLMN归属管理
status: active
---

# LST PLMNMATCH（查询MCC与MNC的归属）

## 功能

**适用NF：SGW-C**

该命令用于查询MCC与MNC的归属。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成PLMN的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLMNMATCH]] · MCC与MNC的归属关系（PLMNMATCH）

## 使用实例

- 如需查询MCC为678下所有MNC的归属关系，执行如下命令：
  ```
  %%LST PLMNMATCH: MCC="678";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
          移动国家码   =  678
          移动网号     =  123
  (Number of results = 1)

  ---    END
  ```
- 查询系统配置中所有MCC与MNC的归属关系，执行如下命令：
  ```
  %%LST PLMNMATCH:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
          移动国家码   =  678
          移动网号     =  123
  (Number of results = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PLMNMATCH.md`
