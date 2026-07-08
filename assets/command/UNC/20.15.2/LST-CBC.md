---
id: UNC@20.15.2@MMLCommand@LST CBC
type: MMLCommand
name: LST CBC（查询CBC）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CBC
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- CBC配置
status: active
---

# LST CBC（查询CBC）

## 功能

**适用网元：MME**

此命令用于查询CBC配置。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入CBC索引号，显示所有CBC的配置。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CBCIDX | CBC索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的CBC的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CBC]] · CBC（CBC）

## 使用实例

输入CBC索引，查询指定的CBC数据：

LST CBC: CBCIDX=0;

```
%%LST CBC: CBCIDX=0;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
          CBC 索引  =  0
      CBC归属的MCC  =  123
      CBC归属的MNC  =  03
        IP地址类型  =  IPv4
          CBC地址1  =  10.10.10.10
          CBC地址2  =  10.10.10.11
          CBC地址3  =  10.10.10.12
          CBC地址4  =  10.10.10.13
          CBC地址5  =  10.10.10.14
          CBC地址6  =  10.10.10.15
          CBC地址7  =  10.10.10.16
          CBC地址8  =  10.10.10.17
           CBC名称  =  CBC1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CBC.md`
