---
id: UNC@20.15.2@MMLCommand@LST NGUSRGRPMEM
type: MMLCommand
name: LST NGUSRGRPMEM（查询5G用户群成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGUSRGRPMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 用户群组成员管理
status: active
---

# LST NGUSRGRPMEM（查询5G用户群成员）

## 功能

**适用NF：AMF**

该命令用于查询5G用户群成员记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [5G用户群成员（NGUSRGRPMEM）](configobject/UNC/20.15.2/NGUSRGRPMEM.md)

## 使用实例

- 查询标识为20的5G用户群成员信息，执行如下命令：
  ```
  %%LST NGUSRGRPMEM: USRGRPID=20;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  用户群组标识  =  20
      IMSI前缀  =  123456
      描述信息  =  SomeTown
  (结果个数 = 1)

  ---    END
  ```
- 查询5G全部用户群成员的信息，执行如下命令：
  ```
  %%LST NGUSRGRPMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  用户群组标识  =  20
      IMSI前缀  =  123456
      描述信息  =  SomeTown
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G用户群成员（LST-NGUSRGRPMEM）_44007023.md`
