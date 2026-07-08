---
id: UNC@20.15.2@MMLCommand@LST PRALSTMEM
type: MMLCommand
name: LST PRALSTMEM（查询PRA列表成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PRALSTMEM
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- PRA区域管理
- PRA区域成员管理
status: active
---

# LST PRALSTMEM（查询PRA列表成员）

## 功能

**适用网元：MME**

该命令用于查询PRA区域位置成员。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指示DNS服务器组ID。<br>数据来源：整网规划<br>取值范围：<br>- “DETAILS(详细报告)”<br>- “SUMMARY(统计信息)”<br>默认值：DETAILS(详细报告) |
| PRAID | PRA标识 | 可选必选说明：条件可选参数<br>参数含义：该参数表示PRA区域的标识<br>数据来源：整网规划<br>取值范围：0x800000～0xFFFFFF<br>默认值：无 |

## 操作的配置对象

- [PRA列表成员（PRALSTMEM）](configobject/UNC/20.15.2/PRALSTMEM.md)

## 使用实例

1. 查询指定PRA标识的成员列表信息。
  LST PRALSTMEM: OUTPUTTYPE=DETAILS, PRAID="0x800001";
  ```
  %%LST PRALSTMEM: OUTPUTTYPE=DETAILS, PRAID="0x800001";%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
             PRA标识  =  0x800001
      位置区标识类型  =  跟踪区标识
          移动国家码  =  123
            移动网号  =  01
      位置区起始标识  =  0x0100
      位置区结束标识  =  0x0200
  (结果个数 = 1)
  ---   END
  ```
2. 查询当前配置的所有PRA标识的列表信息。
  LST PRALSTMEM: OUTPUTTYPE=SUMMARY;
  ```
  %%LST PRALSTMEM: OUTPUTTYPE=SUMMARY;%%
  RETCODE = 0  操作成功。

  统计信息如下
  --------------------------------------
               PRA区域数量  =  4
            跟踪区标识数量  =  276
            宏基站标识数量  =  1001
          家庭基站标识数量  =  1001
   E-UTRAN小区全球标识数量  =  2
          位置成员标识总数  =  2280
  （结果个数 = 1）
  ---   END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PRA列表成员(LST-PRALSTMEM)_72345191.md`
