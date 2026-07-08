---
id: UNC@20.15.2@MMLCommand@LST USNRSVCMD4
type: MMLCommand
name: LST USNRSVCMD4（查询预埋命令4）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USNRSVCMD4
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 预埋命令
status: active
---

# LST USNRSVCMD4（查询预埋命令4）

## 功能

**适用网元：MME**

此命令用于查询S11或S11-U接口的子网配置。

## 注意事项

- 无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FUNNAME | 功能名称 | 可选必选说明：必选参数<br>参数含义：功能名称表示，类似普通的MML命令名<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～31。<br>默认值：无 |
| FUNKEY | 功能KEY参数 | 可选必选说明：必选参数<br>参数含义：功能名称对应的KEY参数。<br>数据来源：本端规划<br>取值范围：字符串形式，区分大小写，字符串长度为1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USNRSVCMD4]] · 预埋命令4（USNRSVCMD4）

## 使用实例

1. 查询当前所有已经添加的实现指定的功能所需要的命令名称以及对应的参数信息，则可以执行以下命令：
  LST USNRSVCMD4:;
  ```
  %%LST USNRSVCMD4:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
     功能名称  =  MOD GLOBALVARIABLE
  功能KEY字段  =  TESTKEY
  字符串参数1  =  str1
  字符串参数2  =  str2
  字符串参数3  =  str3
    整型参数1  =  1
    整型参数2  =  2
    整型参数3  =  3
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询预埋命令4-(LST-USNRSVCMD4)_22715820.md`
