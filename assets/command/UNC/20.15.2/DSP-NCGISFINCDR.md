---
id: UNC@20.15.2@MMLCommand@DSP NCGISFINCDR
type: MMLCommand
name: DSP NCGISFINCDR（查询NCG是否有最终话单文件）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCGISFINCDR
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- NCG最终话单
status: active
---

# DSP NCGISFINCDR（查询NCG是否有最终话单文件）

## 功能

**适用NF：NCG**

该命令用于查询指定业务模块下各通道是否有最终话单文件。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MNAME | 模块名称 | 可选必选说明：可选参数<br>参数含义：用于标识一个业务模块对象，全局唯一。该参数必须先由<br>[ADD MODULE](../../业务配置管理/业务模块/增加业务模块（ADD MODULE）_51174290.md)<br>命令定义，然后才能在此处索引。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCGISFINCDR]] · NCG是否有最终话单文件（NCGISFINCDR）

## 使用实例

查询NCG是否有最终话单文件：

```
DSP NCGISFINCDR:;
```

```
RETCODE = 0  操作成功。
结果如下:
---------
模块名  通道名称  是否有最终话单    
AP64_1  sgwcdr     否               
AP64_1  pgwcdr     否               
AP64_1  ABNORMAL1  是    
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCGISFINCDR.md`
