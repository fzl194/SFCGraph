---
id: UNC@20.15.2@MMLCommand@LST MMECAPBYTA
type: MMLCommand
name: LST MMECAPBYTA（查询基于跟踪区的MME相对权重配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMECAPBYTA
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于跟踪区的MME相对权重
status: active
---

# LST MMECAPBYTA（查询基于跟踪区的MME相对权重配置）

## 功能

**适用网元：MME**

此命令用于查询指定跟踪区下，本MME在MME Pool区内的相对权重值。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：3位的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：2～3位的十进制数字<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMECAPBYTA]] · 基于跟踪区的MME相对权重配置（MMECAPBYTA）

## 使用实例

查看当前配置的全部跟踪区相对权重记录：

LST MMECAPBYTA:;

```
%%LST MMECAPBYTA:;%%
RETCODE = 0  操作成功。

输出结果如下
------------------------
移动国家码    移动网号    跟踪区域码    相对权重

123           03          0x201         100                  
123           03          0x202         255                  
(结果个数 = 2)
---    END
```

查看跟踪区123030200为对应的相对权重记录:

%%LST MMECAPBYTA: MCC="123", MNC="03", TAC="200";%%

```
%%LST MMECAPBYTA: MCC="123", MNC="03", TAC="200";%%
RETCODE = 0  操作成功。

输出结果如下
------------------------
移动国家码  =  123
  移动网号  =  03
跟踪区域码  =  0x200
  相对权重  =  255
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询基于跟踪区的MME相对权重配置(LST-MMECAPBYTA)_26306078.md`
