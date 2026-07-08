---
id: UNC@20.15.2@MMLCommand@LST IMSIHSS
type: MMLCommand
name: LST IMSIHSS（查询IMSI-HSS对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIHSS
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- IMSI-HSS转换信息
status: active
---

# LST IMSIHSS（查询IMSI-HSS对应关系）

## 功能

**适用网元：SGSN、MME**

此命令用于查看IMSI（International Mobile Subscriber Identity）与HSS（Home Subscriber Server）的映射关系表记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：待查询的IMSI前缀。<br>数据来源：全网规划<br>取值范围：1～15位数字<br>默认值：无<br>配置原则：无<br>说明：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [IMSI-HSS对应关系（IMSIHSS）](configobject/UNC/20.15.2/IMSIHSS.md)

## 使用实例

1. 查询系统内IMSI前缀为12301070001与HSS的映射关系表的最大匹配记录：
  LST IMSIHSS: IMSIPRE="12301070001";
  ```
  %%LST IMSIHSS: IMSIPRE="12301070001";%%
  RETCODE = 0  操作成功。

  IMSI和HSS映射表
  ---------------
            IMSI前缀  =  12301070001
             HSS域名  =  example.com
  Diameter路由组索引  =  0
        移动网络名称  =  noname
  (结果个数 = 1)

  ---    END
  ```
2. 查询系统内所有的IMSI与HSS的映射关系表记录：
  LST IMSIHSS:;
  ```
  %%LST IMSIHSS:;%%
  RETCODE = 0  操作成功。

  IMSI和HSS映射表
  ---------------
   IMSI前缀    HSS域名         　　　　　　          Diameter路由组索引    移动网络名称

   1230107000  example.com                           0                     noname      
   1230107     example01.com                         0                     noname      
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI-HSS对应关系(LST-IMSIHSS)_72345053.md`
