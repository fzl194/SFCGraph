---
id: UNC@20.15.2@MMLCommand@LST WEAKPWDDICMEM
type: MMLCommand
name: LST WEAKPWDDICMEM（查询弱口令字典成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: WEAKPWDDICMEM
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
- 弱口令管理
status: active
---

# LST WEAKPWDDICMEM（查询弱口令字典成员）

## 功能

**适用NF：NCG**

该命令用于查询弱口令字典中的成员。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WEAKPWD | 弱口令 | 可选必选说明：可选参数<br>参数含义：用于查询弱口令字典中的成员。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：若不输入，则表示所有查询弱口令字典中所有成员。 |

## 操作的配置对象

- [弱口令字典成员（WEAKPWDDICMEM）](configobject/UNC/20.15.2/WEAKPWDDICMEM.md)

## 使用实例

查询弱口令字典中成员信息 ：

```
LST WEAKPWDDICMEM:;
```

```
RETCODE = 0  操作成功
结果如下:
---------
弱口令            
CSP@gaussdb@2017  
Cspdbg@2017       
Cspdbr@2017       
Huawei#12         
QAZ2wsx@123!      
lgn2020@linux@RD  
(结果个数 = 6)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询弱口令字典成员（LST-WEAKPWDDICMEM）_89575016.md`
