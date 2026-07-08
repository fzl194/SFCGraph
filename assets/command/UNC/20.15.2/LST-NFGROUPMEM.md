---
id: UNC@20.15.2@MMLCommand@LST NFGROUPMEM
type: MMLCommand
name: LST NFGROUPMEM（查询NF组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFGROUPMEM
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例组信息管理
status: active
---

# LST NFGROUPMEM（查询NF组成员）

## 功能

**适用NF：NRF**

该命令用于在NRF上查询NF实例组成员信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF组标识 | 可选必选说明：可选参数<br>参数含义：该参数表示在NRF上配置的NF实例组标识，输入该参数时，可通过LST NFGROUP命令获取。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：该参数表示在NRF上配置的NF实例组成员。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~40。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| NFNAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示在NRF上配置的NF实例组下的成员NF实例的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFGROUPMEM]] · NF组成员（NFGROUPMEM）

## 使用实例

- 在NRF上查询组标识为nfgroup001，实例标识为Instanceid01，实例名称为superom11-v6的NF实例组成员：
  ```
  %%LST NFGROUPMEM: NFGROUPID="nfgroup001", NFINSTANCEID="Instanceid01", NFNAME="superom11-v6";%%
  RETCODE = 0  执行成功

  结果如下
  --------
    NF组标识  =  nfgroup001
  NF实例标识  =  Instanceid01
  NF实例名称  =  superom11-v6
  (结果个数 = 1)

  ---    END
  ```
- 在NRF上查询所有NF实例组成员：
  ```
  %%LST NFGROUPMEM:;%%
  RETCODE = 0  执行成功

  结果如下
  --------
  NF组标识    NF实例标识    NF实例名称    

  nfgroup001  Instanceid01  superom11-v6  
  nfgroup002  Instanceid02  superom11-v3  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF组成员（LST-NFGROUPMEM）_09652297.md`
