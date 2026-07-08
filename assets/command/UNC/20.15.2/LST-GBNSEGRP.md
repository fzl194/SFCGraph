---
id: UNC@20.15.2@MMLCommand@LST GBNSEGRP
type: MMLCommand
name: LST GBNSEGRP（查询NSE和属性模板的关联）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBNSEGRP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb自动配置管理
- NSE属性管理
status: active
---

# LST GBNSEGRP（查询NSE和属性模板的关联）

## 功能

**适用网元：SGSN**

此命令用于显示NSE到属性模板的关联。

## 注意事项

- 此命令执行后立即生效。
- 若不输入参数，则查询所有NSE到属性模板的关联。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPINDEX | 关联索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询NSE到属性模板关联的索引。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBNSEGRP]] · NSE和属性模板的关联（GBNSEGRP）

## 使用实例

1. 显示所有NSE到属性模板的关联：
  LST GBNSEGRP:;
  ```
  %%LST GBNSEGRP:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
   关联索引  起始NSEI  结束NSEI  关联的NSE属性模板索引  描述信息                         

   0         0         99        0                      NULL                             
   1         100       199       1                      huawei                             
   65535     65535     65535     65535                  DEFAULT
  (结果个数 = 3)

  ---    END
  ```
2. 查询 “ 关联索引 ” 为 “0” 的NSE到属性模板的关联：
  LST GBNSEGRP:GRPINDEX=0;
  ```
  %%LST GBNSEGRP:GRPINDEX=0;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
                   关联索引  =  0   
                   起始NSEI  =  0
                   结束NSEI  =  99
      关联的NSE属性模板索引  =  0
                   描述信息  =  NULL 
           
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NSE和属性模板的关联(LST-GBNSEGRP)_26305812.md`
