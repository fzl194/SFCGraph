---
id: UDG@20.15.2@MMLCommand@DSP MEMORYINSPECT
type: MMLCommand
name: DSP MEMORYINSPECT（显示dopra相关内存信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MEMORYINSPECT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP MEMORYINSPECT（显示dopra相关内存信息）

## 功能

该命令用于显示dopra相关内存信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示进程编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| COMMAND | 命令 | 可选必选说明：必选参数<br>参数含义：该参数表示dopra查询命令。当前支持brief命令，PARAMETER1表示分区号，PARAMETER2无意义。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| PARAMETER1 | 参数1 | 可选必选说明：可选参数<br>参数含义：该参数表示dopra查询命令参数1。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| PARAMETER2 | 参数2 | 可选必选说明：可选参数<br>参数含义：该参数表示dopra查询命令参数2。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [dopra相关内存信息（MEMORYINSPECT）](configobject/UDG/20.15.2/MEMORYINSPECT.md)

## 使用实例

显示dopra相关内存信息：

```
DSP MEMORYINSPECT:PROCID=3,COMMAND="brief",PARAMETER1=3
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功 

结果如下:  
---------
内存结果

Info: execute dopra debugging-frame command "show memory 2 3" successfully.

************************************************************************************************************************
PT No.                                  3
PT Name                                 msq_node
PT Algo Name                            DLM
Piece Number                            1
Total Size                              1,600,008(B)
Committed  Size                         1,600,008(B)
Free  Size                              488(B)
Max Block Size                          0(B)
Used Percent=(Total-Free)/Committed     99%
------------------------------------------------------------------------------------------------------------------------
Piece Index     Length(B)                  UsedSize(B)                Begin                End                PhysicMem(B)
         0      1,600,008                  1,596,936                  [  0xffffac91f018] [  0xffffacaa5a20]   1,600,008

************************************************************************************************************************
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示dopra相关内存信息（DSP-MEMORYINSPECT）_59104021.md`
