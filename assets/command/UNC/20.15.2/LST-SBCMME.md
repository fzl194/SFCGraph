---
id: UNC@20.15.2@MMLCommand@LST SBCMME
type: MMLCommand
name: LST SBCMME（查询SBC MME实体）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBCMME
command_category: 查询类
applicable_nf:
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBC MME配置
status: active
---

# LST SBCMME（查询SBC MME实体）

## 功能

**适用网元：CBCF**

此命令用于查询SBC MME实体配置。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入MME索引号，显示所有SBC MME的配置。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的MME的索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBCMME]] · SBC MME实体（SBCMME）

## 使用实例

输入MME索引，查询指定的SBC MME数据：

```
%%LST SBCMME: MMEIDX=0;%%
RETCODE = 0  操作成功。

查询结果如下
-------------------------
          MME 索引  =  0
           MME名称  =  123
      MME POOL标识  =  03
        IP地址类型  =  IPv4
          MME地址1  =  10.10.10.10
          MME地址2  =  10.10.10.11
          MME地址3  =  10.10.10.12
          MME地址4  =  10.10.10.13
          MME地址5  =  10.10.10.14
          MME地址6  =  10.10.10.15
          MME地址7  =  10.10.10.16
          MME地址8  =  10.10.10.17
       MME描述信息  =  MME1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SBCMME.md`
